package Details;
import org.joda.time.DateTime;

public class main {
	DateTime one_cycle = new DateTime();
	DateTime fall_asleep = new DateTime();
	
	// Specifying values for one sleep cycle (1h30m)
	one_cycle = one_cycle.hourofDay().setCopy(1);
	one_cycle = one_cycle.minuteofHour().setCopy(30);

	//Specifying parameters for average time it takes to fall asleep (15m)
	fall_asleep = fall_asleep.minuteofHour().setCopy(15);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new main();
//	public static wakeTime() {
//		
//	}
	}
		
		

}
