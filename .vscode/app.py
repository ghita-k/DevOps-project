from flask import Flask, request, render_template_string
import os
import subprocess

def convert_video(input_path, output_path):
    cmd = ['ffmpeg', '-i', input_path, '-vcodec', 'h264', '-acodec', 'mp2', output_path]
    subprocess.run(cmd, check=True)

app = Flask(__name__)

# Route d'accueil avec le formulaire d'upload vidéo
@app.route('/')
def home():
    return render_template_string("""
        <h1>Bienvenue sur l'application d'upload vidéo</h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="video" />
            <input type="submit" value="Télécharger la vidéo" />
        </form>
    """)

# Route pour gérer l'upload de vidéo
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "Aucun fichier sélectionné", 400
    video = request.files['video']
    
    if video.filename == '':
        return "Aucun fichier sélectionné", 400
    
    # Créer un dossier uploads s'il n'existe pas
    upload_folder = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    input_path = os.path.join(upload_folder, video.filename)
    output_path = os.path.join(upload_folder, f"converted_{video.filename}")
    video.save(input_path)
    convert_video(input_path, output_path)
    return f"Vidéo {video.filename} téléchargée et convertie avec succès", 200

if __name__ == '__main__':
    app.run(debug=True)
