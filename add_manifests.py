from pathlib import Path
import re

js = Path("src/index.js").read_text()
mfs = []
for mf in Path("static", "manifests").glob("*.json"):
    mfs.append(f"{{manifestId: '../manifests/{mf.name}'}}")
mf_str = rf"windows: [{', '.join(mfs)}]"
js = re.sub(r"windows: \[.*\]", mf_str, js, flags=re.DOTALL)
Path("src/index.js").write_text(js)