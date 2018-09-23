

public class Race {

    private double distance;
    private String title;

    Race(String title, double distance){
        this.title = title;
        this.distance = distance;
    }

    public double getDistance() {
        return distance;
    }

    public String getTitle() {
        return title;
    }

}