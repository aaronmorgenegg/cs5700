using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Shapes;

namespace ShapesTests
{
    [TestClass]
    public class CircleTest
    {
        [TestMethod]
        public void TestValidConstruction()
        {
            var circle = new Circle(1, 3, 2.5);
            Assert.AreEqual(1, circle.Center.X);
            Assert.AreEqual(3, circle.Center.Y);
            Assert.AreEqual(2.5, circle.Radius);

            circle = new Circle(new Point(1.23, 4.56), 7.89);
            Assert.AreEqual(1.23, circle.Center.X);
            Assert.AreEqual(4.56, circle.Center.Y);
            Assert.AreEqual(7.89, circle.Radius);
        }

        [TestMethod]
        public void TestInvalidConstruction()
        {
            try
            {
                new Circle(null, 2.5);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid center point", e.Message);
            }

            try
            {
                new Circle(new Point(1, 2), double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }

            try
            {
                new Circle(new Point(1, 2), double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }

            try
            {
                new Circle(new Point(1, 2), Double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }

            try
            {
                new Circle(double.PositiveInfinity, 2, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }

            try
            {
                new Circle(double.NegativeInfinity, 2, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }

            try
            {
                new Circle(Double.NaN, 2, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid x-location point", e.Message);
            }

            try
            {
                new Circle(1, double.PositiveInfinity, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Circle(1, double.NegativeInfinity, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Circle(1, double.NaN, 3);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid y-location point", e.Message);
            }

            try
            {
                new Circle(1, 2, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }

            try
            {
                new Circle(1, 2, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }

            try
            {
                new Circle(1, 2, Double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid radius", e.Message);
            }
        }

        [TestMethod]
        public void TestMove() {
            Circle myCircle = new Circle(1, 2, 5);
            Assert.AreEqual(1, myCircle.Center.X, 0);
            Assert.AreEqual(2, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            myCircle.Move(3, 4);
            Assert.AreEqual(4, myCircle.Center.X, 0);
            Assert.AreEqual(6, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            myCircle.Move(0.123, 0.456);
            Assert.AreEqual(4.123, myCircle.Center.X, 0);
            Assert.AreEqual(6.456, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            myCircle.Move(-0.123, -0.456);
            Assert.AreEqual(4, myCircle.Center.X, 0);
            Assert.AreEqual(6, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            myCircle.Move(-12, -26);
            Assert.AreEqual(-8, myCircle.Center.X, 0);
            Assert.AreEqual(-20, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            try
            {
                myCircle.Move(double.PositiveInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                myCircle.Move(double.NegativeInfinity, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                myCircle.Move(double.NaN, 1);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-x value", e.Message);
            }

            try
            {
                myCircle.Move(1, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                myCircle.Move(1, double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }

            try
            {
                myCircle.Move(1, double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid delta-y value", e.Message);
            }
        }

        [TestMethod]
        public void TestScale() {
            Circle myCircle = new Circle(1, 2, 5);
            Assert.AreEqual(1, myCircle.Center.X, 0);
            Assert.AreEqual(2, myCircle.Center.Y, 0);
            Assert.AreEqual(5, myCircle.Radius, 0);

            myCircle.Scale(3);
            Assert.AreEqual(1, myCircle.Center.X, 0);
            Assert.AreEqual(2, myCircle.Center.Y, 0);
            Assert.AreEqual(15, myCircle.Radius, 0);

            myCircle.Scale(0.2);
            Assert.AreEqual(1, myCircle.Center.X, 0);
            Assert.AreEqual(2, myCircle.Center.Y, 0);
            Assert.AreEqual(3, myCircle.Radius, 0);

            try
            {
                myCircle.Scale(double.PositiveInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (Exception)
            {
                // ignore
            }

            try
            {
                myCircle.Scale(double.NegativeInfinity);
                Assert.Fail("Expected exception not thrown");
            }
            catch (Exception)
            {
                // ignore
            }

            try
            {
                myCircle.Scale(double.NaN);
                Assert.Fail("Expected exception not thrown");
            }
            catch (Exception)
            {
                // ignore
            }
        }

        [TestMethod]
        public void TestComputeArea()
        {
            Circle myCircle = new Circle(1, 2, 5);
            Assert.AreEqual(78.53975, myCircle.ComputeArea(), 0.0001);

            myCircle = new Circle(1, 2, 4.234);
            Assert.AreEqual(56.3185174, myCircle.ComputeArea(), 0.0001);

            myCircle = new Circle(1, 2, 0);
            Assert.AreEqual(0, myCircle.ComputeArea(), 0);

        }
    }
}
