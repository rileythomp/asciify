from app.server import app
import os
 
if __name__ == "__main__":
        print('GOT TO HERE')
        app.run(port = int(os.environ.get('PORT', 17995)))