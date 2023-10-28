terraform {
  backend "s3" {
    bucket = "peaks-terraform-state"
    key    = "peaks-state"
    region = "eu-central-1"
  }
  required_providers {
    random = {
      version = "~>3.5.1"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

provider "random" {
}
