using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Shapes;

namespace ShapesTests
{
    [TestClass]
    public class ValidatorTest
    {
        [TestMethod]
        public void TestValidateDouble()
        {
            Validator.ValidateDouble(123, "Test message");
            Validator.ValidateDouble(0.00123, "Test message");
            Validator.ValidateDouble(-123, "Test message");
            Validator.ValidateDouble(-0.00123, "Test messagee");

            try
            {
                Validator.ValidateDouble(double.PositiveInfinity, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }

            try
            {
                Validator.ValidateDouble(double.NegativeInfinity, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }

            try
            {
                Validator.ValidateDouble(double.NaN, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }
        }

        [TestMethod]
        public void TestValidatePositiveDouble()
        {
            Validator.ValidatePositiveDouble(456, "Test message");
            Validator.ValidatePositiveDouble(0.34523, "Test message");

            try
            {
                Validator.ValidatePositiveDouble(-123, "Negative not allowed");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Negative not allowed", ex.Message);
            }

            try
            {
                Validator.ValidatePositiveDouble(-0.123, "Negative not allowed");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Negative not allowed", ex.Message);
            }

            try
            {
                Validator.ValidatePositiveDouble(double.PositiveInfinity, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }

            try
            {
                Validator.ValidatePositiveDouble(double.NegativeInfinity, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }

            try
            {
                Validator.ValidatePositiveDouble(double.NaN, "Invalid");
                Assert.Fail("Expected exception not thrown");
            }
            catch (ShapeException ex)
            {
                Assert.AreEqual("Invalid", ex.Message);
            }
        }
    }
}
