
public class ProxyDealer implements Lessor{ // 부동산
	private Landlord landlord;
	
	public ProxyDealer(Landlord landlord) { // Origin Server = landlord
		this.landlord = landlord;
	}
	
	@Override
	public Contract contract(int money, Contract contract) { 
		money = money * 10 / 100;
		Contract temp = landlord.contract(money,contract);
		return temp;
	}
	
	public Contract newContract() {
		return new Contract();
	}
}