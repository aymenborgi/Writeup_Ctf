#It's a quick writeup for lazy CTF players
import angr

find = 0x00000000004015F2

avoid = [0x0000000000401419,0x0000000000401621]

proj = angr.Project('./RedVelvet',load_options={'auto_load_libs':False})
path_group = proj.factory.path_group(threads=8)
path_group.explore(find=find, avoid=avoid)

print path_group.found[0].state.posix.dumps(0)

'''
┌─[root@parrot]─[~/Desktop/CTF/codegate]
└──╼ #python Solver.py 
WARNING | 2018-02-04 11:35:57,987 | angr.analyses.disassembly_utils | Your verison of capstone does not support MIPS instruction groups.
WARNING | 2018-02-04 11:35:58,174 | angr.factory | factory.path_group() is deprecated! Please use factory.simgr() instead.
What_You_Wanna_Be?:)_lc_laJ���
                                �*J*�
                                      J

JJ
   �*
'''
