package Details;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

import org.joda.time.DateTime;
import org.joda.time.Duration;
import org.joda.time.format.DateTimeFormat;

public class sleepyTime {
	static DateTime  one_cycle = new DateTime();
	static DateTime fall_asleep = new DateTime();
	public static void main(String[] args) {
//		DateTime  one_cycle = new DateTime();
//		DateTime fall_asleep = new DateTime();
		
		// Specifying values for one sleep cycle (1h30m)
		one_cycle = one_cycle.hourOfDay().setCopy(1);
		one_cycle = one_cycle.minuteOfHour().setCopy(30);
	
		//Specifying parameters for average time it takes to fall asleep (15m)
		fall_asleep = fall_asleep.minuteOfHour().setCopy(15);
		
		
		wake_time();
	}
	public static void wake_time() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Specify your wake time in HH:MM format: ");
		String wake = sc.next();
		sc.close();
		
		org.joda.time.format.DateTimeFormatter dt = DateTimeFormat.forPattern("HH:mm");
				
		DateTime joda_wake = dt.parseDateTime(wake);
		
		
		for (int i = 0; i <= 6; i++) {
			joda_wake = joda_wake.plusHours(1).plusMinutes(30);
			System.out.println(joda_wake);
		}
		
		System.out.println(joda_wake.clock;
		System.out.println(joda_wake.getMinuteOfDay());
		
	
	
	}
		
		

}
