package examples.shapes;

import org.junit.Test;

import static org.junit.Assert.*;

public class PointTest {

    @Test
    public void testValidConstruction() throws Exception {
        Point p1 = new Point(1,2);
        assertEquals(1, p1.getX(), 0);
        assertEquals(2, p1.getY(), 0);

        p1 = new Point(1.111,2.222);
        assertEquals(1.111, p1.getX(), 0);
        assertEquals(2.222, p1.getY(), 0);
    }

    @Test
    public void testInvalidConstruction() {

        try {
            new Point(1,Double.POSITIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Point(1,Double.NEGATIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Point(1,Double.NaN);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Point(Double.POSITIVE_INFINITY, 1);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Point(Double.NEGATIVE_INFINITY, 1);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            new Point(Double.NaN, 1);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

    }

    @Test
    public void testMoveX() throws Exception {
        Point p1 = new Point(1,2);

        p1.moveHorizon(10);
        assertEquals(11, p1.getX(), 0);
        assertEquals(2, p1.getY(), 0);

        p1.moveHorizon(0.1234);
        assertEquals(11.1234, p1.getX(), 0);
        assertEquals(2, p1.getY(), 0);

        p1.moveHorizon(-20);
        assertEquals(-8.8766, p1.getX(), 0);
        assertEquals(2, p1.getY(), 0);

        p1.moveHorizon(0);
        assertEquals(-8.8766, p1.getX(), 0);
        assertEquals(2, p1.getY(), 0);

        try {
            p1.moveHorizon(Double.POSITIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.moveHorizon(Double.NEGATIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.moveHorizon(Double.NaN);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

    }

    @Test
    public void testMoveY() throws Exception {
        Point p1 = new Point(1,2);

        p1.moveVert(10);
        assertEquals(1, p1.getX(), 0);
        assertEquals(12, p1.getY(), 0);

        p1.moveVert(0.1234);
        assertEquals(1, p1.getX(), 0);
        assertEquals(12.1234, p1.getY(), 0);

        p1.moveVert(-20);
        assertEquals(1, p1.getX(), 0);
        assertEquals(-7.8766, p1.getY(), 0);

        p1.moveVert(0);
        assertEquals(1, p1.getX(), 0);
        assertEquals(-7.8766, p1.getY(), 0);

        try {
            p1.moveVert(Double.POSITIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.moveVert(Double.NEGATIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.moveVert(Double.NaN);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

    }

    @Test
    public void testMove() throws Exception {
        Point p1 = new Point(1,2);

        p1.move(10, 20);
        assertEquals(11, p1.getX(), 0);
        assertEquals(22, p1.getY(), 0);

        p1.move(0.222, 0.333);
        assertEquals(11.222, p1.getX(), 0);
        assertEquals(22.333, p1.getY(), 0);

        p1.move(-0.222, -0.333);
        assertEquals(11, p1.getX(), 0);
        assertEquals(22, p1.getY(), 0);

        p1.move(-20, -30);
        assertEquals(-9, p1.getX(), 0);
        assertEquals(-8, p1.getY(), 0);

        try {
            p1.move(1, Double.POSITIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.move(1, Double.NEGATIVE_INFINITY);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.move(1, Double.NaN);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.move(Double.POSITIVE_INFINITY, 1);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.move(Double.NEGATIVE_INFINITY,1 );
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

        try {
            p1.move(Double.NaN,1);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // ignore
        }

    }
    
}