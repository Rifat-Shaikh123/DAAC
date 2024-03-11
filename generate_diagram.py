from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service
from diagrams.k8s.storage import PV, PVC, StorageClass

def generate_diagram_from_code(diagram_code, output_filename):
    # Execute the provided code within the context of a Diagram
    exec(diagram_code)

    # Generate the diagram
    with Diagram("", show=False):
        pass  # Diagram code executed in the exec() function

    # Save the diagram to the output filename
    diagram = Diagram("", show=False)
    diagram.render(filename=output_filename)

if __name__ == "__main__":
    # Example diagram code (replace this with your actual diagram code)
    code = """
with Diagram("Stateful Architecture"):
    with Cluster("Apps"):
        svc = Service("svc")
        sts = StatefulSet("sts")

        apps = []
        for _ in range(3):
            pod = Pod("pod")
            pvc = PVC("pvc")
            pod - sts - pvc
            apps.append(svc >> pod >> pvc)

    apps << PV("pv") << StorageClass("sc")
"""

    # Output filename for the generated diagram
    output_filename = "dynamic_diagram.png"

    # Generate the diagram from the provided code
    generate_diagram_from_code(code, output_filename)
