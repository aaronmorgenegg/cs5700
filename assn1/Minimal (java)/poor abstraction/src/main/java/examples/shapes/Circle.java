package examples.shapes;

@SuppressWarnings("WeakerAccess")
public class Circle {
    private Point center;
    private double radius;

    public Circle(double x, double y, double radius) throws ShapeException {
        Validator.validatePositiveDouble(radius, "Invalid radius");
        center = new Point(x, y);
        this.radius = radius;
    }

    public Circle(Point center, double radius) throws ShapeException {
        Validator.validatePositiveDouble(radius, "Invalid radius");
        if (center==null)
            throw new ShapeException("Invalid center point");
        this.center = center;
        this.radius = radius;
    }

    public Circle(double radius, Point center) throws ShapeException {
        this(center, radius);
    }

    public Point getCenter() { return center; }
    public double getRadius() { return radius; }

    public void move(double deltaX, double deltaY) throws ShapeException {
        center.move(deltaX, deltaY);
    }

    public void scale(double scaleFactor) throws ShapeException {
        Validator.validatePositiveDouble(scaleFactor, "Invalid scale factor");
        radius *= scaleFactor;
    }
}
