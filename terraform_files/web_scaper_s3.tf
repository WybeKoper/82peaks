resource "random_pet" "bucket_name" {
  length    = 3
  separator = "-"
}


resource "aws_s3_bucket" "peaks-data-bucket" {
  bucket        = "peaks-bucket-${random_pet.bucket_name.id}"
  force_destroy = true
}
