namespace Shapes
{
    public class Point
    {
        public double X { get; private set; }
        public double Y { get; private set; }

        public Point(double x, double y)
        {
            Validator.ValidateDouble(x, "Invalid x-location point");
            Validator.ValidateDouble(y, "Invalid y-location point");
            X = x;
            Y = y;
        }

        /**
        * Move the point in the x direction
        *
        * @param deltaX            The delta amount to move the point -- must be a valid double
        * @throws ShapeException   Exception thrown if the parameter is invalid
        */
        public void MoveX(double deltaX)         {
            Validator.ValidateDouble(deltaX, "Invalid delta-x value");
            X += deltaX;
        }

        /**
         * Move the point in the y direction
         *
         * @param deltaY            The delta amount to move the point -- must be a valid double
         * @throws ShapeException   Exception thrown if the parameter is invalid
         */
        public void MoveY(double deltaY)
        {
            Validator.ValidateDouble(deltaY, "Invalid delta-y value");
            Y += deltaY;
        }

        /**
         * Move the point
         *
         * @param deltaX            The delta amount to move the point in the x direction -- must be a valid double
         * @param deltaY            The delta amount to move the point in the y direction -- must be a valid double
         * @throws ShapeException   Exception throw if any parameter is invalid
         */ 
        public void Move(double deltaX, double deltaY)
        {
            MoveX(deltaX);
            MoveY(deltaY);
        }

        /**
         * Copy the point
         * @return                  A new point with same x and y locations
         * @throws ShapeException   Should never thrown because the current x and y are valid
         */
        public Point Copy()
        {
            return new Point(X, Y);
        }

}
}
