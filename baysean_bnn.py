import bif.bif_parser as bif_parser
import prettytable
import pydotplus
from IPython.core.display import Image
from bayesian.bbn import *

name = 'asia'
module_name = bif_parser.parse(name)
module = __import__(module_name)
bg = module.create_bbn()


def show_graphgiz_image(graphviz_data):
    graph = pydotplus.graph_from_dot_data(graphviz_data)
    graph.write_png('temp.png')
    return 'temp.png'
sf=bg.get_graphviz_source()
Image(filename=show_graphgiz_image(sf))

gu=make_undirected_copy(bg)
m1=make_moralized_copy(gu,bg)
s2=m1.get_graphviz_source()
Image(filename=show_graphgiz_image(s2))


cliques, elimination_ordering = triangulate(m1, priority_func)
s2=m1.get_graphviz_source()
Image(filename=show_graphgiz_image(s2))

jt=bg.build_join_tree()
sf=jt.get_graphviz_source()
Image(filename=show_graphgiz_image(sf))


# Creating the initial cluster and initialize potentials
assignments = jt.assign_clusters(bg)
jt.initialize_potentials(assignments,bg)

# Running the message passing bit using the propagate method
jt.propagate()


either_clust=[i for i in jt.clique_nodes for v in i.variable_names if v =='either']
either_clust[0].potential_tt


potE1=either_clust[0].potential_tt

# Function to return the sum for a specific assignment, such as 'bronc,yes'
sum_assignments=lambda imap,tup:sum([v for k,v in imap.iteritems() for i in k if i == tup])

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potE1,('either',i)) for i in ['yes','no']]

print 'Either: yes ', yes/float(yes+no)," no ", no/float(yes+no)

either_clust[1].potential_tt

potE1=either_clust[1].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potE1,('either',i)) for i in ['yes','no']]

print 'Either: yes ', yes/float(yes+no)," no ", no/float(yes+no)


either_clust[2].potential_tt



potE2=either_clust[2].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potE2,('either',i)) for i in ['yes','no']]

print 'Either: yes ', yes/float(yes+no)," no ", no/float(yes+no)


either_clust[3].potential_tt



potE3=either_clust[3].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potE3,('either',i)) for i in ['yes','no']]

print 'Either: yes ', yes/float(yes+no)," no ", no/float(yes+no)



either_clust[4].potential_tt


potE4=either_clust[4].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potE4,('either',i)) for i in ['yes','no']]

print 'Either: yes ', yes/float(yes+no)," no ", no/float(yes+no)


bronc_clust=[i for i in jt.clique_nodes for v in i.variable_names if v =='bronc']
bronc_clust[0].potential_tt


bronc_clust[1].potential_tt


pot2=bronc_clust[1].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(pot2,('bronc',i)) for i in ['yes','no']]

print 'bronc: yes ', yes/float(yes+no)," no ", no/float(yes+no)



smoke_clust=[i for i in jt.clique_nodes for v in i.variable_names if v =='smoke']
smoke_clust[0].potential_tt



pot=smoke_clust[0].potential_tt

# Function to return the sum for a specific assignment, such as 'bronc,yes'
sum_assignments=lambda imap,tup:sum([v for k,v in imap.iteritems() for i in k if i == tup])

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(pot,('smoke',i)) for i in ['yes','no']]

print 'smoke: yes ', yes/float(yes+no)," no ", no/float(yes+no)



smoke_clust[1].potential_tt



pot2=smoke_clust[1].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(pot2,('smoke',i)) for i in ['yes','no']]

print 'smoke: yes ', yes/float(yes+no)," no ", no/float(yes+no)



tub_clust=[i for i in jt.clique_nodes for v in i.variable_names if v =='tub']
tub_clust[0].potential_tt



pot=tub_clust[0].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(pot,('tub',i)) for i in ['yes','no']]

print 'Tub: yes ', yes/float(yes+no)," no ", no/float(yes+no)



tub_clust[1].potential_tt



tub_clust[1].potential_tt
potT1=tub_clust[1].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potT1,('tub',i)) for i in ['yes','no']]

print 'Tub: yes ', yes/float(yes+no)," no ", no/float(yes+no)



lung_clust=[i for i in jt.clique_nodes for v in i.variable_names if v =='lung']
lung_clust[0].potential_tt



pot=lung_clust[0].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(pot,('lung',i)) for i in ['yes','no']]

print 'Lung: yes ', yes/float(yes+no)," no ", no/float(yes+no)

lung_clust[1].potential_tt

potL1=lung_clust[1].potential_tt

# Get the sum for bronc=yes and bronc=no
yes,no=[sum_assignments(potL1,('lung',i)) for i in ['yes','no']]

print 'Lung: yes ', yes/float(yes+no)," no ", no/float(yes+no)
