from diagrams import Diagram, Cluster, Edge
from diagrams.azure.general import Managementgroups
from diagrams.azure.general import Subscriptions
from diagrams.azure.identity import ActiveDirectory

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
with Diagram("Azure Tenant Design", direction="TB"):
    tenant = ActiveDirectory("Tenant AD")  
    topGroup = Managementgroups("Main\r\nManagement Group")
    sandbox = Subscriptions("Sandbox\r\nSubscription")
 
    with Cluster("Business Units"):
        with Cluster("Unit1"):
          mainGroup = Managementgroups("Unit1\r\nManagement Group")
          topGroup >> mainGroup
          with Cluster("Project1"):
            group = Managementgroups("Project1\r\nManagement Group")
            sub = [Subscriptions("Project1\r\nDev/Test\r\nSubscription"), Subscriptions("Project1\r\nProduction\r\nSubscription")]
            group - sub
            mainGroup >> group
 
          with Cluster("Project2"):
            group = Managementgroups("Project2\r\nManagement Group")
            sub = [Subscriptions("Project2\r\nDev/Test\r\nSubscription"), Subscriptions("Project2\r\nProduction\r\nSubscription")]
            group - sub
            mainGroup >> group
 
        with Cluster("Infrastructure"):
          group = Managementgroups("Infrastructure\r\nManagement Group")
          sub = [Subscriptions("Test\r\nSubscription"), Subscriptions("Infrastructure\r\nProduction\r\nSubscription")]
          group - sub
          topGroup >> group
 
    tenant >> topGroup >> sandbox
"""

    # Output filename for the generated diagram
    output_filename = "dynamic_diagram.png"

    # Generate the diagram from the provided code
    generate_diagram_from_code(code, output_filename)
