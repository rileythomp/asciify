from app.server import app
import os
 
if __name__ == "__main__":
        app.run(port = int(os.environ.get('PORT', 17995)))