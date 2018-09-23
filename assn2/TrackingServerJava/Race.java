

public class Race extends java.util.Observable {

    private double distance;
    private String title;

    Race(String title, double distance){
        this.title = title;
        this.distance = distance;
    }

    public double getDistance() {
        return distance;
    }

    public void setDistance(double distance) {
        this.distance = distance;
        setChanged();
        notifyObservers();
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
        setChanged();
        notifyObservers();
    }

}