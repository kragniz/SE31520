class WinesController < ApplicationController
  before_action :set_wine, only: [:show, :edit, :update, :destroy]

  # GET /wines
  # GET /wines.json
  def index
    #@wines = Wine.all
    @wines = Wine.page(params[:page]).order(:name).per(9)
  end

  # GET /wines/1
  # GET /wines/1.json
  def show
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_wine
      @wine = Wine.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def wine_params
      params.require(:wine).permit(:name, :image, :long_description, :country, :grape, :vegetarian, :size, :price, :short_description)
    end
end
