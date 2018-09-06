package examples.shapes;

import org.junit.Test;

import static org.junit.Assert.*;

public class LineTest {

    @Test
    public void testValidConstruction() throws Exception {
        Point p1 = new Point(1,2);
        Point p2 = new Point(4, 10);

        Line myLine = new Line(p1, p2);
        assertSame(p1, myLine.getPoint1());
        assertSame(p2, myLine.getPoint2());

        myLine = new Line(p1, p1);
        assertSame(p1, myLine.getPoint1());
        assertSame(p1, myLine.getPoint2());

        p1 = new Point(1.4,2.5);
        p2 = new Point(4.6, 10.7);
        myLine = new Line(p1, p2);
        assertSame(p1, myLine.getPoint1());
        assertSame(p2, myLine.getPoint2());

        myLine = new Line(1, 3.33, 4.444, 5.5555);
        assertEquals(1, myLine.getPoint1().getX(), 0);
        assertEquals(3.33, myLine.getPoint1().getY(), 0);
        assertEquals(4.444, myLine.getPoint2().getX(), 0);
        assertEquals(5.5555, myLine.getPoint2().getY(), 0);
    }

    @Test
    public void testInvalidConstruction() throws ShapeException {
        Point p1 = new Point(1,2);
        Point p2 = new Point(4, 10);

        try {
            new Line(p1, null);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Line(null, p2);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }
    }


    @Test
    public void testMove() throws ShapeException {
        Line myLine = new Line(1, 2, 4, 10);

        myLine.move(3, 4);
        assertEquals(4, myLine.getPoint1().getX(), 0);
        assertEquals(6, myLine.getPoint1().getY(), 0);
        assertEquals(7, myLine.getPoint2().getX(), 0);
        assertEquals(14, myLine.getPoint2().getY(), 0);

        myLine.move(.4321, .7654);
        assertEquals(4.4321, myLine.getPoint1().getX(), 0);
        assertEquals(6.7654, myLine.getPoint1().getY(), 0);
        assertEquals(7.4321, myLine.getPoint2().getX(), 0);
        assertEquals(14.7654, myLine.getPoint2().getY(), 0);

        myLine.move(-0.4321, -0.7654);
        assertEquals(4, myLine.getPoint1().getX(), 0);
        assertEquals(6, myLine.getPoint1().getY(), 0);
        assertEquals(7, myLine.getPoint2().getX(), 0);
        assertEquals(14, myLine.getPoint2().getY(), 0);
    }

    @Test
    public void testComputeLength() throws ShapeException {

        Line myLine = new Line(1, 2, 4, 10);
        assertEquals(8.544, myLine.computeLength(), 0.001);

        myLine = new Line(1, 2, 1, 2);
        assertEquals(Math.sqrt(0), myLine.computeLength(), 0);

        myLine = new Line(3, -2, -4, 10);
        assertEquals(13.892, myLine.computeLength(), 0.001);
    }

    @Test
    public void testComputeSlope() throws ShapeException {
        Line myLine = new Line(2, 2, 4, 10);
        assertEquals(0.25, myLine.computeSlope(), 0.1);

        myLine = new Line(2, 2, 4, 10);
        assertEquals(0.25, myLine.computeSlope(), 0.1);

        myLine = new Line(2, 2, 2, 4);
        assertEquals(0, myLine.computeSlope(), 0.1);

        myLine = new Line(2, 2, 4, 2);
        assertEquals(Double.POSITIVE_INFINITY, myLine.computeSlope(), 0.1);

        myLine = new Line(4, 2, 2, 2);
        assertEquals(Double.NEGATIVE_INFINITY, myLine.computeSlope(), 0.1);

        myLine = new Line(2, 2, 2, 2);
        assertEquals(Double.NaN, myLine.computeSlope(), 0.1);
    }

}