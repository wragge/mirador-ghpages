from pathlib import Path
import re

js = Path("src/index.js").read_text()
mfs = []
if match := re.search(r"windows: \[(.*?)\]", js):
    mfs.append(match.group(1))
for mf in Path("manifests").glob("*.json"):
    mfs.append(f"{{manifestId: 'manifests/{mf.name}'}}")
mf_str = rf"windows: [{', '.join([m for m in mfs if m])}]"
js = re.sub(r"windows: \[.*?\]", mf_str, js, flags=re.DOTALL)
Path("src/index.js").write_text(js)