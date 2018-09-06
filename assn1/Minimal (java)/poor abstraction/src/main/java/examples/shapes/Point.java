package examples.shapes;

@SuppressWarnings("WeakerAccess")
public class Point {
    private double x;
    private double y;

    public Point(double x, double y) throws ShapeException {
        Validator.validateDouble(x, "Invalid x-location");
        Validator.validateDouble(y, "Invalid y-location");
        this.x = x;
        this.y = y;
    }

    public double getX() { return x; }
    public double getY() { return y; }

    public void moveHorizon(double deltaX) throws ShapeException {
        Validator.validateDouble(deltaX, "Invalid delta-x value");
        x += deltaX;
    }

    public void moveVert(double deltaY) throws ShapeException {
        Validator.validateDouble(deltaY, "Invalid delta-y value");
        y += deltaY;
    }

    public void move(double deltaX, double deltaY) throws ShapeException {
        moveHorizon(deltaX);
        moveVert(deltaY);
    }
}
