package examples.shapes;

@SuppressWarnings("WeakerAccess")
public class Line {
    private Point linePoint1;
    private Point linePoint2;

    public Line(double x1, double y1, double x2, double y2) throws ShapeException {
        linePoint1 = new Point(x1, y1);
        linePoint2 = new Point(x2, y2);
    }

    public Line(Point linePoint1, Point linePoint2) throws ShapeException {
        if (linePoint1 ==null || linePoint2 ==null)
            throw new ShapeException("Invalid Point");

        this.linePoint1 = linePoint1;
        this.linePoint2 = linePoint2;
    }

    public Point getLinePoint1() { return linePoint1; }

    public Point getLinePoint2() { return linePoint2; }

    public void move(double deltaX, double deltaY) throws ShapeException {
        linePoint1.move(deltaX, deltaY);
        linePoint2.move(deltaX, deltaY);
    }

    public double dist() {
        return Math.sqrt(Math.pow(linePoint2.getX() - linePoint1.getX(), 2) +
                         Math.pow(linePoint2.getY() - linePoint1.getY(), 2));
    }
}
