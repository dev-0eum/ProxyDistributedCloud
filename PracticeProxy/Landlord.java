public class Landlord implements Lessor{ // 집주인
	public int account = 0;
	private String sign;
	
	public Landlord(String sign) {
		this.account = 0;
		this.sign = sign;
	}
	
	// @Override
	public Contract contract(int money, Contract contract) {
		account += money;
		contract.setSignOfLessor(sign);
		return contract;
	}
}