#!/usr/bin/env python3
"""Build a small agent-ready prompt.md with relative image paths."""

import argparse
import hashlib
import mimetypes
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=Path, required=True, help="UTF-8 copyable prompt text")
    parser.add_argument("--output", type=Path, required=True, help="Resulting prompt.md")
    parser.add_argument("--version", required=True, help="Extraction package version")
    parser.add_argument("--status", required=True, choices=["draft", "reviewed", "pass"])
    parser.add_argument(
        "--image",
        action="append",
        required=True,
        metavar="ROLE=images/filename.png",
        help="A model-generated prompt input image; repeat for each role",
    )
    args = parser.parse_args()

    output = args.output.resolve()
    root = output.parent
    image_root = (root / "images").resolve()
    if args.text.resolve().parent != root:
        parser.error("The copyable text file must be beside the output prompt.md.")
    prompt = args.text.read_text(encoding="utf-8").strip()
    if not prompt:
        parser.error("The copyable prompt text is empty.")

    assets = []
    seen = set()
    for item in args.image:
        if "=" not in item:
            parser.error(f"Expected ROLE=images/path: {item}")
        role, relative = item.split("=", 1)
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", role) or role in seen:
            parser.error(f"Invalid or duplicate image role: {role}")
        seen.add(role)
        path = (root / relative).resolve()
        if not path.is_relative_to(image_root) or not path.is_file():
            parser.error(f"Image must exist under {image_root}: {relative}")
        mime, _ = mimetypes.guess_type(path.name)
        if mime not in {"image/png", "image/jpeg", "image/webp"}:
            parser.error(f"Unsupported image MIME type: {path}")
        raw = path.read_bytes()
        assets.append(
            {
                "role": role,
                "relative": path.relative_to(root).as_posix(),
                "mime": mime,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
            }
        )
        if assets[-1]["relative"] not in prompt:
            parser.error(f"Image path must appear in the copyable prompt: {assets[-1]['relative']}")

    lines = [
        "# 多模态产品提示词",
        "",
        f"版本：{args.version}  |  复测状态：{args.status}",
        "",
        "[网页端与桌面 Agent 手动测试步骤](manual-test-guide.md)",
        "",
        "## 可复制文字提示词",
        "",
        "桌面 Agent：以本文件所在目录为基准解析相对路径，实际读取图片文件并作为图片输入。网页端：按角色上传图片，再复制下面的文字。请连同 images/ 目录一起移动或分享本文件。",
        "",
        "````text",
        prompt,
        "````",
        "",
        "## 图片路径",
        "",
        "| 角色 | 图片文件 | MIME | SHA-256 | 字节数 |",
        "|---|---|---|---|---:|",
    ]
    for asset in assets:
        lines.append(
            f"| {asset['role']} | [{asset['relative']}]({asset['relative']}) | "
            f"{asset['mime']} | `{asset['sha256']}` | {asset['bytes']} |"
        )
    lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote {output} with {len(assets)} images.")


if __name__ == "__main__":
    main()
