import Image from "next/image";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Gallery | MGBW Group - Moments & Milestones",
  description:
    "A visual journey through our business achievements, manufacturing excellence, and community impact.",
};

const galleryItems = [
  {
    image: "/images/gallery/tax-award.jpg",
    title: "Income Tax Department Karnataka & Goa – Best Tax Payer Award",
    desc: "Income tax department Karnataka & Goa best tax payer award.",
  },
  {
    image: "/images/gallery/manava-rathna.jpg",
    title: "Manava Rathna Award",
    desc: "Advanced quality control processes ensuring product excellence.",
  },
  {
    image: "/images/gallery/udyam-shri.jpg",
    title: "Udyam Shri 2023 – Business Excellence Award",
    desc: "For exemplary contributions in the field of business and enterprise.",
  },
  {
    image: "/images/gallery/excise-award.jpg",
    title: "Appreciation Award – Central Excise & Service Tax, Mangalore",
    desc: "In recognition of outstanding contribution to the Commissionerate of Central Excise, Mangalore.",
  },
  {
    image: "/images/gallery/exporter-award.jpg",
    title: "Best Exporter Award – Tobacco Board, Government of India",
    desc: "For achieving highest performance (2nd Position) in Exporting of Beedis.",
  },
];

export default function GalleryPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gray-900 text-white py-20 text-center px-4">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">
          MGBW Group Gallery
        </h1>
        <p className="text-lg font-light opacity-80 max-w-2xl mx-auto">
          A visual journey through our business achievements, manufacturing
          excellence, and community impact across all our ventures.
        </p>
      </section>

      {/* Gallery Grid */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-6xl mx-auto grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {galleryItems.map((item) => (
            <div
              key={item.title}
              className="bg-gray-50 rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition"
            >
              <div className="relative h-56">
                <Image
                  src={item.image}
                  alt={item.title}
                  fill
                  className="object-cover"
                />
              </div>
              <div className="p-6">
                <h3 className="font-bold text-lg mb-2">{item.title}</h3>
                <p className="text-gray-600 text-sm">{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
