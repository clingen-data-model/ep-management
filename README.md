# ep-management

ClinGen has grown dramatically from its inception from X clinical domain working groups (CDWG) and Y expert panels (EP) in 2015 to M CDWGs and N EPs in 2020.  This rapid growth has necessitated the introduction of administrative processes and procedures to ensure consistency in EP practices and operations.  FDA recognition of variant interpretations (TODO: need advice for language here) in 2018 brought increased rigor and administrative complexity to the [variant EP application process](https://clinicalgenome.org/site/assets/files/3635/vcep_protocol_v_12_5_19.pdf).  The growth of administrative requirements has put substantial strain on members of the CDWG Oversight Committee (OC) as well as CDWG and EP coordinators.  Coordinators must maintain records of group membership, contributor training, conflict of interest disclosures, and more in addition to overseeing curation activities.  This increase in administrative responsibilities eats time scientists could be spending practicing science.

## Goals
The intention of this project is to develop tooling to automate and streamline the administrative activities of OC members and CDWG and EP coordinators.  Specifically, we will design software to  support the creation and maintenance of CDWG gene and variant expert panels by 
 * Guide coordinators through the application process with a structured application workflow.
 * Co-locating documentation, help resources, and best-in-class examples
 * Managing conflict of interest (COI) requirements
 * Scheduling annual updates
 * Automating notifications and reminders
 * Facilitating collaboration and feedback on application documents such as EP scope definition and AMCG/AMP guideline specifications
 * Integrate with other ClinGen information systems to streamline interoperability

## In this repository
 * prototype1 - An oversimplified prototype domain model built on top of the eventsourcing package
 

See the full [requirements](documentation/requirements.md) for details on uses cases.
