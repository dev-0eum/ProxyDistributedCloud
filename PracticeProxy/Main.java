
public class Main {
    public static void main(String[] args){
        Landlord landlord = new Landlord("홍길동"); // 예제에서는 사용자 쪽에서 타겟 객체를 생성했지만 실제로는 프로시 내에서 생성 및 관리할 수 있음.
        ProxyDealer dealer = new ProxyDealer(landlord);

        Contract contract = dealer.newContract(); // 계약서 종이를 들고 옴.
        contract.setSignOfTenant("김대차"); // 대차인 작성.
        contract = dealer.contract(100000,contract); // 프록시를 통해 계약 진행.
        System.out.println(contract.getSignOfLessor());
        System.out.println(contract.getSignOfTenant());

    }

}