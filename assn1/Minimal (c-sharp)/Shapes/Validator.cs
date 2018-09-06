using System;

namespace Shapes
{
    public class Validator
    {
        public static void ValidateDouble(double value, string errorMessage)
        {
            if (double.IsInfinity(value) || double.IsNaN(value))
                throw new ShapeException(errorMessage);
        }

        public static void ValidatePositiveDouble(double value, String errorMessage) 
        {
                ValidateDouble(value, errorMessage);
                if (value<0)
                    throw new ShapeException(errorMessage);
        }
    }
}
