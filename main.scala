import chisel3._
import circt.stage.ChiselStage
import java.io._

class MyModule(width: Int) extends Module {
  val io = IO(new Bundle {
    val in  = Input(UInt(width.W))
    val out = Output(UInt(width.W))
  })

  io.out := io.in
}

object Hello {
  def main(args: Array[String]) : Unit = {
    val writer = new FileWriter(new File("echo.sv"))
    val sv = ChiselStage.emitSystemVerilog(new MyModule(args(0).toInt))
    writer.write(sv)
    writer.close()
  }
}
