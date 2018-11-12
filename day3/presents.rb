require 'matrix'
require 'pry'
binding.pry
class Map
  attr_reader :grid, :position, :housecount
  def initialize
    @grid = [[1]]
    @position = [0,0]
    @housecount = 1
  end

  def move(dir)
    case dir
    when ?v
      @position[0] += 1
      if @position[0] == @grid.length
        temp = Matrix[*@grid]
        temp = Matrix.vstack(temp, Matrix.row_vector(Array.new(@grid[0].length) { 0 } ))
        @grid = temp.to_a
      end
    when ?^
      @position[0] -= 1
      if @position[0] < 0
        temp = Matrix[*@grid]
        temp = Matrix.vstack(Matrix.row_vector(Array.new(@grid[0].length) { 0 }), temp)
        @grid = temp.to_a
        @position[0] = 0
      end
    when ?>
      @position[1] += 1
      if @position[1] == @grid[@position[0]].length
        temp = Matrix[*@grid]
        temp = Matrix.hstack(temp, Matrix.column_vector(Array.new(@grid.length) { 0 } ))
        @grid = temp.to_a
      end
    when ?<
      @position[1] -= 1
      if @position[1] < 0
        temp = Matrix[*@grid]
        temp = Matrix.hstack(Matrix.column_vector(Array.new(@grid.length) { 0 } ))
        @grid = temp.to_a
        @position[1] = 0
      end
    end
    @housecount += 1 if @grid[@position[0]][@position[1]] == 0
    @grid[@position[0]][@position[1]] += 1
  end
end

santa = Map.new
instructions = File.readlines('./input', :chomp=> true)[0]
instructions.each_char { |i| santa.move(i) }

return santa.housecount
