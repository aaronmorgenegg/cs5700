

public class Athlete extends java.util.Observable {

    private int bib;
    private String first_name;
    private String last_name;
    private int age;
    private String gender;
    private Double start_time;
    private Double end_time;
    private String status;
    private int distance;


    Athlete(int bib, Double start_time, String first_name, String last_name, String gender, int age){
        this.bib = bib;
        this.start_time = start_time;
        this.first_name = first_name;
        this.last_name = last_name;
        this.age = age;
        this.gender = gender;
        this.end_time = 0.0;
        this.status = "Registered";
        this.distance = 0;
    }

    public int getBib() {
        return bib;
    }

    public Double getStartTime() { return start_time; }

    public Double getEndTime() { return end_time; }

    public void setEndTime(double time){
        this.end_time = time;
        setChanged();
        notifyObservers();
    }

    public String getFirstName() {
        return first_name;
    }

    public String getLastName() {
        return last_name;
    }

    public String getGender() {
        return gender;
    }

    public int getAge() {
        return age;
    }

    public Double getDistance() { return this.distance; }

    public void setDistance(distance){
        this.distance = distance;
        setChanged();
        notifyObservers();
    }

    public String getStatus() { return this.status;}

    public void setStatus(String status){
        this.status = status;
        setChanged();
        notifyObservers();
    }

}