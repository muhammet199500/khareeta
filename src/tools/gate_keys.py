"""Add N new entry codes to src/gate.json and print them once.
   The codes themselves are never written to the repository: copy them to a private place.
   usage: python3 src/tools/gate_keys.py 5"""
import hashlib, json, os, secrets, sys
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'gate.json')
A = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
g = json.load(open(P)) if os.path.exists(P) else {'on': True, 'salt': secrets.token_hex(8), 'keys': {}}
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nums = [int(k[1:]) for k in g['keys']] or [0]
for i in range(max(nums) + 1, max(nums) + 1 + n):
    c = ''.join(secrets.choice(A) for _ in range(8))
    g['keys'][f'k{i:02d}'] = hashlib.sha256(f"{g['salt']}:{c}".encode()).hexdigest()
    print(f'k{i:02d}  {c[:4]}-{c[4:]}')
json.dump(g, open(P, 'w'), indent=1)
