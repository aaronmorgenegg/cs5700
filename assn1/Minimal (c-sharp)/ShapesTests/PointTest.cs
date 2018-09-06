using Microsoft.VisualStudio.TestTools.UnitTesting;
using Shapes;

namespace ShapesTests
{
    [TestClass]
    public class PointTest
    {
        [TestMethod]
        public void TestValidConstruction()
        {
            var p1 = new Point(1, 2);
            Assert.AreEqual(1, p1.X, 0);
            Assert.AreEqual(2, p1.Y, 0);

            p1 = new Point(1.111, 2.222);
            Assert.AreEqual(1.111, p1.X, 0);
            Assert.AreEqual(2.222, p1.Y, 0);
        }

        [TestMethod]
        public void TestInvalidConstruction() {
            try
            {
                new Point(1, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Point(1, double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Point(1, double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Point(double.PositiveInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }

            try
            {
                new Point(double.NegativeInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }

            try
            {
                new Point(double.NaN, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }
        }

        [TestMethod]
        public void TestMoveX() {
            Point p1 = new Point(1, 2);

            p1.MoveX(10);
            Assert.AreEqual(11, p1.X, 0);
            Assert.AreEqual(2, p1.Y, 0);

            p1.MoveX(0.1234);
            Assert.AreEqual(11.1234, p1.X, 0);
            Assert.AreEqual(2, p1.Y, 0);

            p1.MoveX(-20);
            Assert.AreEqual(-8.8766, p1.X, 0);
            Assert.AreEqual(2, p1.Y, 0);

            p1.MoveX(0);
            Assert.AreEqual(-8.8766, p1.X, 0);
            Assert.AreEqual(2, p1.Y, 0);

            try
            {
                p1.MoveX(double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }


            try
            {
                p1.MoveX(double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                p1.MoveX(double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }
        }

        [TestMethod]
        public void TestMoveY() {
            Point p1 = new Point(1, 2);

            p1.MoveY(10);
            Assert.AreEqual(1, p1.X, 0);
            Assert.AreEqual(12, p1.Y, 0);

            p1.MoveY(0.1234);
            Assert.AreEqual(1, p1.X, 0);
            Assert.AreEqual(12.1234, p1.Y, 0);

            p1.MoveY(-20);
            Assert.AreEqual(1, p1.X, 0);
            Assert.AreEqual(-7.8766, p1.Y, 0);

            p1.MoveY(0);
            Assert.AreEqual(1, p1.X, 0);
            Assert.AreEqual(-7.8766, p1.Y, 0);

            try
            {
                p1.MoveY(double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                p1.MoveY(double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                p1.MoveY(double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }
        }

        [TestMethod]
        public void TestMove() {
            Point p1 = new Point(1, 2);

            p1.Move(10, 20);
            Assert.AreEqual(11, p1.X, 0);
            Assert.AreEqual(22, p1.Y, 0);

            p1.Move(0.222, 0.333);
            Assert.AreEqual(11.222, p1.X, 0);
            Assert.AreEqual(22.333, p1.Y, 0);

            p1.Move(-0.222, -0.333);
            Assert.AreEqual(11, p1.X, 0);
            Assert.AreEqual(22, p1.Y, 0);

            p1.Move(-20, -30);
            Assert.AreEqual(-9, p1.X, 0);
            Assert.AreEqual(-8, p1.Y, 0);

            try
            {
                p1.Move(1, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                p1.Move(1, double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                p1.Move(1, double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                p1.Move(double.PositiveInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                p1.Move(double.NegativeInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                p1.Move(double.NaN, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }
        }

        [TestMethod]
        public void TestCopy() {
            Point p1 = new Point(-123.45, -23.45);
            Assert.AreEqual(-123.45, p1.X, 0);
            Assert.AreEqual(-23.45, p1.Y, 0);

            Point p2 = p1.Copy();
            Assert.AreNotSame(p1, p2);
            Assert.AreEqual(p1.X, p2.X, 0);
            Assert.AreEqual(p1.Y, p2.Y, 0);
        }
    }
}
