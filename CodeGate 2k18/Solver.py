#It's a quick writeup for lazy CTF players
import angr

find = 0x00000000004015F2

avoid = [0x0000000000401419,0x0000000000401621]

proj = angr.Project('./RedVelvet',load_options={'auto_load_libs':False})
path_group = proj.factory.path_group(threads=8)
path_group.explore(find=find, avoid=avoid)

print path_group.found[0].state.posix.dumps(0)
