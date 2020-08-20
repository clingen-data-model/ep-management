# Expert Panel Management Requirements

[back to project readme](../readme.md)

The requirements below are based on interviews with multiple stakeholders representing multiple roles relevant to the creation and maintanence of Expert Panels.  This is intended to be a descriptive, not prescriptive description of user's needs to effectively manage ClinGen expert panels.

## Definition of terms and user roles
* ACMG - American college of edial Genetics and Genomics
  * ACMG/AMP Guidelines - General guidelines for interpreting the pathogenicity of variants.
  * ACMG/AMP guideline specifications (specifications) - VCEP specifications of the AMCG/AMP Guidelines applicable to the VCEP's genes of interest.
* CDWG (Clinical Domain Working Group) - 
* CDWG Oversight committee (OC) - 
* Co-chairs - 
* COI - Conflict of interest`
* Expert Panel (EP) - 
* EP Members - Members of an expert panel  
Members include:
  * Coordinator - An EP member who coordinates the activities of the expert panel.  This is usually the point person on the EP for the application process
  * Biocurator - Does biocuration for the EP
  * 
* GCEP - Gene Curation Expert Panel
* SOP - Standard Operating Procedure
* SVI - Sequence Variant Interpretation
  * Rule Specification Review Committee - Reviews and approves VCEP ACMG specifications 
* VCEP - Variant Curation Expert Panel


## Expert Panel Application Management
The EP application process differs between GCEPs and VCEPs.  GCEPs only need to define the scope and membership of their group (EP Definition).  VCEPs must also develop and pilot AMCG guidelines.  

### Starting an application
* A person unaffiliated with ClinGen needs to be able to start an EP application.
* A person affiliated with ClinGen needs to be able to start an EP application.
* A OC member should be notified of a new application being started.

### EP Definition
* A coordinator needs to be able to provide a "working" name for the EP
* A coordinator needs to add members to their expert panel
  * An EP member should have the following data:
    * First and last name
    * Email address
    * Institution
    * Area and type of expertise
    * Role (i.e. Biocurator, Coordinator, Leadership, etc.)
  * Added members should be notified that they have been added and given information about how to log in
  * EP members must be able to complete a COI form.
    * EP members should be reminded to complete their COI form 2 weeks after they have been added to an EP if it is not already completed
* A coordinator should be able to update EP members
* A coordinator should be able to delete EP members
* A coordinator should be able to define the scope of the EP
* A coordinator needs information about how to complete the application
  * A coordinator would like "gold-standard" examples of an application

* A coordinator needs to be able to define an SOP 
* An authorized user should be able to comment on and SOP

### AMCG/AMP Guideline Specifications
* A coordinator should be able to submit draft AMCG guidelines in a structured way
  * ACMG/AMP guidelines have the following structure:
     * applicable genes
     * Description for criteria
        * PVS1, PS1-4, PM1-6, PP1-5, BA1, BS1-4, BP1-6
    * Rules for pathogenic and benign classification
* An authorized user should be able to comment on guidelines draft.
* Comments should be related to a specific draft of a guidelines section

### Specifications Pilot
* ?

## Expert panel maintainence
* A coordinator should be able to see a list of EP members including the following information:
  * Name, email, COI status, role

### Annual Review
* A coordinator must review EP members and make any updates that have not been recorded.
* A coordinator must complete any new application sections that they have not previously completed.

### Comments
* An authorized user should be able to reply to a comment on any part of an application.

## Integration and Data Sharing
* Authorized external systems should be able to request information about an expert panel including:
  * Application status
  * List of members with name, email, and role
  * Associated CDWG
* EP events should be produced sent to the Clingen Data Exchange including:
  * Application progress updates
  * EP Member updates (additions, edits, removal)
* Should be able to link GCI/VCI affiliation with EP.
* Should be able to share approved Guidelines w/ Clingen Specification Repository
  