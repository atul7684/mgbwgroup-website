import Image from "next/image";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Shukra Beedies LLP | Premium Traditional Handcrafted Beedis",
  description:
    "Built on quality, discipline, and trust since 1982. Crafted with consistency, trusted for generations.",
};

const whySetsApart = [
  "Decades of focused manufacturing",
  "Clean and compliant production units",
  "Steady supply chain practices",
  "Skilled labor backed by experienced supervision",
  "Efficient product packaging & labeling",
];

const whyPartner = [
  "Over 40 years of industry presence",
  "Professional setup with reliable compliance",
  "Clear pricing structures and supply timelines",
  "Responsive distributor support",
  "Packaging adaptability for bulk markets",
];

export default function ShukraBeediPage() {
  return (
    <>
      {/* Hero */}
      <section className="relative h-[70vh] flex items-center justify-center bg-gray-900">
        <div className="absolute inset-0">
          <Image
            src="/images/business/shukrabeedi/shukrabeedi-hero.jpg"
            alt="Shukra Beedies LLP"
            fill
            className="object-cover opacity-40"
            priority
          />
        </div>
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">
            Shukra Beedies LLP
          </h1>
          <p className="text-lg font-light mb-2">
            Crafted with Consistency. Trusted for Generations.
          </p>
          <p className="text-base opacity-80">
            Built on quality, discipline, and trust since 1982
          </p>
          <Link
            href="/contact"
            className="inline-block mt-8 px-8 py-3 bg-pink-600 text-white rounded-full hover:bg-pink-700 transition"
          >
            Become a Distributor
          </Link>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-pink-600 text-white py-8">
        <div className="max-w-4xl mx-auto grid grid-cols-3 gap-4 text-center">
          <div>
            <div className="text-2xl font-bold">100+</div>
            <div className="text-sm opacity-90">Distributors</div>
          </div>
          <div>
            <div className="text-2xl font-bold">80+</div>
            <div className="text-sm opacity-90">Years of Business</div>
          </div>
          <div>
            <div className="text-2xl font-bold">100%</div>
            <div className="text-sm opacity-90">Industry Compliant</div>
          </div>
        </div>
      </section>

      {/* About */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">About Shukra Beedies LLP</h2>
          <div className="text-gray-600 leading-relaxed space-y-4">
            <p>
              Incorporated in{" "}
              <strong className="text-gray-900">November 1982</strong>, Shukra
              Beedies Limited Liability Partnership was established with a clear
              vision — to manufacture high-quality beedies with consistency and
              integrity. With over four decades of operational experience, we
              have established a trusted reputation among both consumers and
              distributors.
            </p>
            <p>
              Backed by traditional expertise and operational discipline, Shukra
              Beedies continues to cater to regional and national markets,
              delivering reliable volumes with precision.
            </p>
          </div>
        </div>
      </section>

      {/* What Sets Apart */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">What Sets Us Apart</h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {whySetsApart.map((item) => (
              <div
                key={item}
                className="flex items-center gap-3 p-4 bg-white rounded-lg shadow-sm"
              >
                <span className="text-pink-600 font-bold text-xl">✓</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Production */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">Production Capability</h2>
          <p className="text-gray-600 mb-6">
            Shukra Beedies operates with a focus on efficiency and output
            quality, employing skilled workers and adhering to structured
            processes.
          </p>
          <div className="grid sm:grid-cols-2 gap-4">
            {[
              "Product uniformity",
              "Tendu leaf quality checks",
              "Humidity-controlled storage",
              "Timely dispatches for local and regional distribution",
            ].map((item) => (
              <div key={item} className="flex items-center gap-3 p-3">
                <span className="text-pink-600">•</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Partner */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">Why Partner with Us</h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {whyPartner.map((item) => (
              <div
                key={item}
                className="flex items-center gap-3 p-4 bg-white rounded-lg shadow-sm"
              >
                <span className="text-pink-600 font-bold text-xl">✓</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-pink-600 text-white text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">
          Partner With Us
        </h2>
        <p className="mb-6 opacity-90 max-w-xl mx-auto">
          Your market. Our product. Let&apos;s build a trusted presence
          together.
        </p>
        <Link
          href="/contact"
          className="inline-block px-8 py-3 bg-white text-pink-600 rounded-full font-semibold hover:bg-gray-100 transition"
        >
          Contact Us
        </Link>
      </section>
    </>
  );
}
