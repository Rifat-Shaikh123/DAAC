from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service
from diagrams.k8s.storage import PV, PVC, StorageClass

def generate_stateful_architecture_diagram():
    with Diagram("Stateful Architecture", filename="https://github.com/Rifat-Shaikh123/DAAC/Stateful_Architecture.png", show=False):
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

if __name__ == "__main__":
    generate_stateful_architecture_diagram()
