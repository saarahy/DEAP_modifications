# DEAP_modifications
Adding the subtree crossover 
1) On algorithms.py you have to import the cx_mut.py<br>
<code>import cx_mut</code>

2) On the same file, you have to change the line:
<code>offspring = varAnd(offspring, toolbox, cxpb, mutpb)</code><br>
to:<br>
<code>offspring = cx_mut.varOr(offspring, toolbox, cxpb, mutpb)

3) On the principal file "principal.py" (in this case), you have to import the cxSubtree.py file: <br>
<code>import cxSubtree as cx</code>

4) On the same file you have to change this line: <br>
<code>toolbox.register("mate", gp.cxOnePoint)</code><br>
to this line: <br>
<code>toolbox.register("mate", cx.cxSubtree)</code>


5) On "gp.py" file import the neat_gp.py file:<br>
<code>from neat_gp import neat</code><br>
And on the PrimitiveTree Class add the following parameter <code>(neat)</code>: <br>
<code>class PrimitiveTree(gp.PrimitiveTree, neat):</code>

6) Inside the class we will find the <code>init</code> function, we will add the following besides the <code>list.__init__(self, content)</code> line:<br>
<code> self.off_cx=None<br>
        self.off_mut=None</code>