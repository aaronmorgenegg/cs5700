using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Shapes;

namespace ShapesTests
{
    [TestClass]
    public class LineTest
    {
        [TestMethod]
        public void TestValidConstruction()
        {
            var p1 = new Point(1,2);
            var p2 = new Point(4, 10);


            var myLine = new Line(p1, p2);
           
            Assert.AreSame(p1, myLine.Point1);
            Assert.AreSame(p2, myLine.Point2);

            myLine = new Line(p1, p1);
            Assert.AreSame(p1, myLine.Point1);
            Assert.AreSame(p1, myLine.Point2);

            p1 = new Point(1.4,2.5);
            p2 = new Point(4.6, 10.7);
            myLine = new Line(p1, p2);
            Assert.AreSame(p1, myLine.Point1);
            Assert.AreSame(p2, myLine.Point2);

            myLine = new Line(1, 3.33, 4.444, 5.5555);
            Assert.AreEqual(1, myLine.Point1.X, 0);
            Assert.AreEqual(3.33, myLine.Point1.Y, 0);
            Assert.AreEqual(4.444, myLine.Point2.X, 0);
            Assert.AreEqual(5.5555, myLine.Point2.Y, 0);
        }

        [TestMethod]
        public void TestInvalidConstruction()
        {
            var p1 = new Point(1,2);
            var p2 = new Point(4, 10);

            try {
                new Line(p1, null);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid point", e.Message);
            }

            try {
                new Line(null, p2);
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException e)
            {
                Assert.AreEqual("Invalid point", e.Message);
            }
        }

        [TestMethod]
        public void TestMove()
        {
            var myLine = new Line(1, 2, 4, 10);

            myLine.Move(3, 4);
            Assert.AreEqual(4, myLine.Point1.X, 0);
            Assert.AreEqual(6, myLine.Point1.Y, 0);
            Assert.AreEqual(7, myLine.Point2.X, 0);
            Assert.AreEqual(14, myLine.Point2.Y, 0);

            myLine.Move(.4321, .7654);
            Assert.AreEqual(4.4321, myLine.Point1.X, 0);
            Assert.AreEqual(6.7654, myLine.Point1.Y, 0);
            Assert.AreEqual(7.4321, myLine.Point2.X, 0);
            Assert.AreEqual(14.7654, myLine.Point2.Y, 0);

            myLine.Move(-0.4321, -0.7654);
            Assert.AreEqual(4, myLine.Point1.X, 0);
            Assert.AreEqual(6, myLine.Point1.Y, 0);
            Assert.AreEqual(7, myLine.Point2.X, 0);
            Assert.AreEqual(14, myLine.Point2.Y, 0);
        }

        [TestMethod]
        public void TestComputeLength()
        {

            var myLine = new Line(1, 2, 4, 10);
            Assert.AreEqual(8.544, myLine.ComputeLength(), 0.001);

            myLine = new Line(1, 2, 1, 2);
            Assert.AreEqual(Math.Sqrt(0), myLine.ComputeLength(), 0);

            myLine = new Line(3, -2, -4, 10);
            Assert.AreEqual(13.892, myLine.ComputeLength(), 0.001);
        }

        [TestMethod]
        public void TestComputeSlope() { 
            var myLine = new Line(2, 2, 4, 10);
            Assert.AreEqual(4, myLine.ComputeSlope(), 0.1);

            myLine = new Line(2, 2, 10, 4);
            Assert.AreEqual(0.25, myLine.ComputeSlope(), 0.1);

            myLine = new Line(2, 2, 4, 0);
            Assert.AreEqual(-1, myLine.ComputeSlope(), 0.1);

            myLine = new Line(2, 2, 2, 4);
            Assert.AreEqual(double.PositiveInfinity, myLine.ComputeSlope(), 0.1);

            myLine = new Line(2, 4, 2, 2);
            Assert.AreEqual(double.NegativeInfinity, myLine.ComputeSlope(), 0.1);

            myLine = new Line(2, 2, 2, 2);
            Assert.IsTrue(double.IsNaN(myLine.ComputeSlope()));
        }
    }
}
