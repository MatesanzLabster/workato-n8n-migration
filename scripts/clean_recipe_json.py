import json, sys, os

def try_parse(s):
    if not isinstance(s, str):
        return s
    st = s.strip()
    if not st or st[0] not in '{[':
        return s
    try:
        return json.loads(st)
    except Exception:
        return s

def deep(obj):
    if isinstance(obj, dict):
        return {k: deep(try_parse(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep(try_parse(v)) for v in obj]
    return obj

def main():
    for fname in sys.argv[1:]:
        if os.path.getsize(fname) == 0:
            print("SKIP empty:", fname)
            continue
        with open(fname, encoding='utf-8') as f:
            raw = json.load(f)
        normalized = deep(raw)
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(normalized, f, indent=2, ensure_ascii=False)
        print("OK:", fname)

if __name__ == "__main__":
    main()
