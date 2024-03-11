from diagrams import Diagram

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
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.azure.general import Subscriptions, Usericon, Resourcegroups, Shareddashboard, Templates, Tags
from diagrams.generic.blank import Blank
from diagrams.azure.devops import Devops, Repos, Pipelines
from diagrams.azure.compute import CloudServicesClassic, ContainerInstances, KubernetesServices, VMLinux, VMWindows, Disks, SAPHANAOnAzure
from diagrams.azure.database import SQLServers, CosmosDb, CacheForRedis
from diagrams.azure.network import NetworkWatcher, VirtualNetworks, NetworkSecurityGroupsClassic, ServiceEndpointPolicies
from diagrams.azure.identity import ADPrivilegedIdentityManagement, AccessReview, Groups,AppRegistrations
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.security import KeyVaults
from diagrams.azure.web import AppServices
from diagrams.azure.storage import BlobStorage
with Diagram("Managed Cloud Services", direction="LR"):

    with Cluster(""):
            Subscriptions1=Subscriptions("TSI Operations Subscription",height="0.5", width="0.5",fontsize="7")
            Custom1=Custom(" ", "./Screenshot 2024-02-09 132946.png", height="1.5", width="1.5")
            Pim1 = ADPrivilegedIdentityManagement("PIM", height="0.5", width="0.5",fontsize="7")
            Cluster1 = [Subscriptions1 - Edge(style='invis') - [Repos("Repos", height="0.5", width="0.5",fontsize="7"),Pipelines("Pipelines", height="0.5", width="0.5",fontsize="7"),Devops("Azure DevOps", height="0.5", width="0.5",fontsize="7"),Custom("TCI Framework", "./AzureAutomation.png",height="0.5", width="0.5",fontsize="7"),Pim1,Usericon("\nAAD IAM",height="0.5", width="0.5",fontsize="7")]- Edge(style='invis') - Custom1, AccessReview("", height="0.25", width="0.25", pos='0,0')]

    
    with Cluster(" "):
        Subscriptions2 = Subscriptions("Client Manged Subscription", height="0.5", width="0.5",fontsize="7")
        Shareddashboard1 = Shareddashboard("TSI Shared Dashboard", height="0.5", width="0.5",fontsize="7")
        
        with Cluster("   ",direction="TB"):
            AzureMonitor1= Custom("", "./AzureMonitor.png",height="0.5", width="0.5")
            Resourcegroups2 = [Resourcegroups("MCSAz-[1234]-P-EUW-RG-Glabal", height="0.5", width="0.5",fontsize="8"),
                              AzureMonitor1- Edge(style='invis') - LogAnalyticsWorkspaces("", height="0.5", width="0.5") - Edge(style='invis') - Custom("", "./Azuremetrics.png", height="0.5", width="0.5")]
        with Cluster("  ", direction="TB"):
            Vnet1= VirtualNetworks("", height="0.5", width="0.5",fontsize="7")
            Resource_mgmt= Resourcegroups("MCSAz-[1234]-P-EUW-RG-MGMT",height="0.5", width="0.5", fontsize="8")
            RecoveryServicesVaults1=RecoveryServicesVaults("", height="0.5", width="0.5") - Edge(style='invis')
            Resourcegroups1 = [
                Resource_mgmt,
                RecoveryServicesVaults1 - Custom("", "./AzureAutomation.png", height="0.5", width="0.5")
                - Edge(style='invis') - NetworkWatcher("",height="0.5", width="0.5") -
                Edge(style='invis') - Vnet1 ]
        AzurePolicy = Custom("TSI Azure Policy Defination Framework", "./AzurePolicyDefination.png", height="0.5", width="0.5",fontsize="7")
        json = Templates("TSI Gallery Template", height="0.5", width="0.5",fontsize="7")
          
        with Cluster("    ",direction="TB"):
            Tag1=Tags("",height="0.5", width="0.5")
            NSG1= NetworkSecurityGroupsClassic("",height="0.5", width="0.5")
            Tag1- Edge(style='invis') - NSG1 - Edge(style='invis') - Custom("", "./User Subscription.png", height="0.5", width="0.5") - Edge(style='invis') - ServiceEndpointPolicies("",height="0.5", width="0.5")- Edge(style='invis') - KeyVaults("", height="0.5", width="0.5")
            Resourcegroups4711=Resourcegroups("MANO-P-EUW-0000001-PROJECTXAPP4711", height="0.5", width="0.5", fontsize="8")
            Resourcegroups4711- Edge(style='invis') - ContainerInstances("", height="0.5", width="0.5")- Edge(style='invis') - KubernetesServices("", height="0.5", width="0.5", fontsize="8") 
        Resourcegroups1- Edge(style='invis') - Resourcegroups4711
        
        with Cluster("     ",direction="TB"):
            NSG2 = NetworkSecurityGroupsClassic("", height="0.5", width="0.5", fontsize="8")
            Resourcegroups4 = Resourcegroups("MANO-P-EUW-0000001-VMSQLIaaS", height="0.5", width="0.5", fontsize="8")
            Tags("",height="0.5", width="0.5") - Edge(style='invis') - NSG2 - Edge(style='invis') - Custom("", "./User Subscription.png",height="0.5", width="0.5", fontsize="8") - Edge(style='invis') - ServiceEndpointPolicies("", height="0.5", width="0.5") - Edge(style='invis') - KeyVaults("", height="0.5", width="0.5")
            VMLinux("", height="0.5", width="0.5") - Edge(style='invis') - Disks("", height="0.5", width="0.5") - Edge(style='invis') - VMWindows("", height="0.5", width="0.5") - Edge(style='invis') - SQLServers("",height="0.5", width="0.5") - Edge(style='invis') - SAPHANAOnAzure("", height="0.5", width="0.5")
            Resourcegroups1 - Edge(style='invis') - Resourcegroups4
       
        with Cluster("PaaS"):
            Resourcegroups5 = Resourcegroups("MANO-P-EUW-0000001-PaaS", height="0.5", width="0.5", fontsize="8")    
            NSG3 = NetworkSecurityGroupsClassic("",height="0.5", width="0.5") 
            Tags("", height="0.5", width="0.5",pos='0,0!') - Edge(style='invis') - NSG3  - Edge(style='invis') - Custom("", "./User Subscription.png", height="0.5", width="0.5") - Edge(style='invis') - ServiceEndpointPolicies("", height="0.5", width="0.5") - Edge(style='invis') - KeyVaults("", height="0.5", width="0.5")
            AppServices("",height="0.5", width="0.5" ) - Edge(style='invis') - BlobStorage("", height="0.5", width="0.5") - Edge(style='invis') - CosmosDb("", height="0.5", width="0.5" ) - Edge(style='invis') - CacheForRedis("", height="0.5", width="0.5" )
            Resourcegroups1 - Edge(style='invis') - Resourcegroups5
    Connection=Custom("","./Connection.png",height="5", width="5")        
    Custom1 >> Edge(style='invis') >>Connection
    Connection>> Edge(style='invis') >>Resource_mgmt
    
    Vnet1\
            >> Edge(style="dotted")>>[NSG1,NSG2,NSG3]
                              
    """

    # Output filename for the generated diagram
    output_filename = "dynamic_diagram.png"

    # Generate the diagram from the provided code
    generate_diagram_from_code(code, output_filename)
