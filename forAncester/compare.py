from modeller import *

env = environ()
aln = alignment(env)
for (pdb, chain) in (('4eam', 'A'), ('5i3d', 'C'), ('4ha4', 'A'),
                     ('3wdp', 'P'), ('3wq8', 'A'), ('1qvb', 'A')):
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)