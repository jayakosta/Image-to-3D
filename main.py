from PIL import Image
from rembg import remove
import trimesh
import pyrender
import numpy as np

def remove_background(image_path):
    try:
        input_image = Image.open(image_path)
        output_image = remove(input_image)
        output_image.save("processed_image.png")
        print("Background removed and saved as processed_image.png")
    except Exception as e:
        print(f"Error during background removal: {e}")

def generate_simple_3d_model():
    try:
        mesh = trimesh.creation.icosphere(radius=1.0)
        mesh.export("output_model.obj")
        print("3D model saved as output_model.obj")
        return mesh
    except Exception as e:
        print(f"Error during 3D model generation: {e}")

def visualize_model(mesh):
    try:
        print("Starting visualization...")
        scene = pyrender.Scene()
        pyrender_mesh = pyrender.Mesh.from_trimesh(mesh)
        scene.add(pyrender_mesh)
        viewer = pyrender.Viewer(scene, use_raymond_lighting=True)
        print("Model visualization completed successfully.")
    except Exception as e:
        print(f"Error during 3D model visualization: {e}")

if __name__ == "__main__":
    image_path = input("Enter path to your image (JPG/PNG): ").strip()
    remove_background(image_path)
    mesh = generate_simple_3d_model()
    visualize_model(mesh)
