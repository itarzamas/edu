from edu import edu
@edu.route('/') 
@edu.route('/index') 
def index():
         return "Hello, World!"