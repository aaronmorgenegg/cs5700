

public class Race {

    private int distance;
    private String title;

    Race(String title, int distance){
        this.title = title;
        this.distance = distance;
    }

    public int getDistance() {
        return distance;
    }

    public String getTitle() {
        return title;
    }

}