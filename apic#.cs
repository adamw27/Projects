[HttpGet]
        public async Task<ActionResult<string>> ([FromQuery] int , [FromQuery] int , [FromQuery] int , [FromQuery] int )
        {
            string connectionString = this.configuration.GetValue<string>();
            Int32 rv = -1;

            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    await connection.OpenAsync();
                    SqlCommand command = connection.CreateCommand();
                    command.CommandType = CommandType.StoredProcedure;
                    command.CommandText = "";
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    //                command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    SqlParameter parameterReturnValue = new SqlParameter();
                    parameterReturnValue.Direction = ParameterDirection.ReturnValue;
                    command.Parameters.Add(parameterReturnValue);
                    await command.ExecuteNonQueryAsync();
                    rv = Int32.Parse(parameterReturnValue.Value.ToString());
                    await connection.CloseAsync();
                }
            }
            catch (Exception ex)
            {
                rv = -2;
            }
            return rv.ToString();
        }

[HttpGet]
        public async Task<ActionResult<string>> ([FromQuery] int  = 0, [FromQuery] int  = 0, [FromQuery] int  = 0, [FromQuery] int  = 0, [FromQuery] int  = 0, [FromQuery] int  = 0)
        {
            string connectionString = this.configuration.GetValue<string>();
            Int32 rv = -1;

            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    await connection.OpenAsync();
                    SqlCommand command = connection.CreateCommand();
                    command.CommandType = CommandType.StoredProcedure;
                    command.CommandText = "";
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    //                command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    command.Parameters.AddWithValue();
                    SqlParameter parameterReturnValue = new SqlParameter();
                    parameterReturnValue.Direction = ParameterDirection.ReturnValue;
                    command.Parameters.Add(parameterReturnValue);
                    await command.ExecuteNonQueryAsync();
                    rv = Int32.Parse(parameterReturnValue.Value.ToString());
                    await connection.CloseAsync();
                }
            }
            catch (Exception ex)
            {
                rv = -2;
            }
            return rv.ToString();
        }