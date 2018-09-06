using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Shapes;

namespace ShapesTests
{
    [TestClass]
    public class ShapeExeptionTest
    {
        [TestMethod]
        public void TestConstruction()
        {
            var exception = new ShapeException("test message");
            Console.WriteLine(exception.Message);
            Assert.AreEqual("test message", exception.Message);
        }
    }
}
