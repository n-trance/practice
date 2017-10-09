import java.lang.Math;

class Degrees {
	
	public static float degrees(float hour, float min) {
		float hr_deg	= (hour + min/hour) * 30;
		float min_deg	= min * 6;
		float deg = Math.abs(hr_deg - min_deg);
		return (Math.min(deg, 360 - deg));
	}

	public static void main(String[] args) {
		System.out.println("hello");
		System.out.println(degrees(3,0));
		System.out.println(degrees(12,0));
		System.out.println(degrees(1,10));
		System.out.println(degrees(3,27));
	}
}
