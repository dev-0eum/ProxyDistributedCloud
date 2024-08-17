public class Contract{
    private String signOfLessor;
	private String signOfTenant;

    public Contract(){}

    public Contract(String signOfLessor, String signOfTenant){
        this.signOfLessor = signOfLessor;
        this.signOfTenant = signOfTenant;
    }

    // Getter
    public String getSignOfLessor() {
		return signOfLessor;
	}
	
	public String getSignOfTenant() {
		return signOfTenant;
	}
	
    // Setter
	public void setSignOfLessor(String signOfLessor) {
		this.signOfLessor = signOfLessor;
	}
	
	public void setSignOfTenant(String signOfTenant) {
		this.signOfTenant = signOfTenant;
	}
}