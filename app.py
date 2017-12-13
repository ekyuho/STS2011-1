from flask import Flask, render_template
from flask_cors import cross_origin
import tensorflow as tf
import numpy as np
app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

graph = 0
sess = 0
tensor_x = 0
tensor_y = 0

@app.route("/")
def paint():
    return render_template('paint.html')
    #return 'hi'

@app.route("/predict/<data>", methods=['GET', 'POST'])
@cross_origin()
def predict(data):
    val = 0
    print(data)
    splited = data.split('_')
    print('len', len(splited))
    data = np.array([(1.0 - float(i) / 255.0) for i in splited])
    data = np.tile(data, (128, 1))
    print (data[0])

    result = sess.run(tensor_y, feed_dict= {
        tensor_x: data
    })
    print ('result', result)
    # prediction
    return str(result[0])

def load_graph(filename):
    with tf.gfile.GFile(filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def)
    return graph

if __name__ == "__main__":
    graph = load_graph('frozen_graph.pb')
    for op in graph.get_operations():
        print(op.name)
    tensor_x = graph.get_tensor_by_name('import/INPUT_IMAGE:0')
    tensor_y = graph.get_tensor_by_name('import/OUTPUT:0')
    sess = tf.Session(graph=graph)
    app.run(host='0.0.0.0')